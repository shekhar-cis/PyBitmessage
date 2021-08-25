#!/bin/bash

if [ -z "${1}" ]; then
    echo "Command not specified"
    exit 1
fi

function import_gpg_key
{
    username="${1}"
    echo "Importing GPG key for ${username}"
    f=`mktemp`
    curl -s https://api.github.com/users/${username}/gpg_keys -o ${f}
    keyid="`jq -r '.[0].key_id' ${f}`"
    jq -r '.[0].raw_key' ${f}| gpg --import
    fpr=`gpg -k ${keyid}|grep -E '[A-F0-9]{40}'`
    gpg --quick-lsign-key ${fpr}
    rm -f ${f}
}

function mergepullrequest
{
    echo "Merging PR ${1}"
    curbranch=$(git status|head -1|cut -d\  -f3-)

    upstream="v0.6"

    git pull --all
    git checkout -B upstream-$upstream --track upstream/"$upstream"
    git fetch upstream pull/"$1"/head:"$1"
    git merge --verify-signatures --ff-only -m "Merge PR $1 into $upstream" "$1"
    #git checkout -B $curbranch --track origin/$curbranch
    git checkout -B "$curbranch"
}

function rebase_open_prs
{
    pulljs=$(mktemp)
    username=$(git remote get-url origin| sed -E 'sx.*[:/](.+)/PyBitmessage(.git)?x\1x')
    echo "My user name is $username"
    head="$(curl -s https://api.github.com/repos/Bitmessage/PyBitmessage/branches/v0.6 | jq ".commit.sha"|cut -d\" -f2)"
    echo "head is $head"
    curl -s https://api.github.com/repos/Bitmessage/PyBitmessage/pulls -o "$pulljs"
    pulls=$(jq ".[] | select(.user.login == \"$username\").number" < "$pulljs")
    git pull --all --no-commit
    for pr in $pulls; do
        echo -n "PR $pr is mine, "
        parent="$(jq ".[] | select(.number == $pr).base.sha" < "$pulljs"|cut -d\" -f2)"
        if [ "$parent" != "$head" ]; then
            echo -n "not up to date, "
            branch="$(jq ".[] | select(.number == $pr).head.ref" < "$pulljs"|cut -d\" -f2)"
            echo -n "rebasing branch $branch, "
            git checkout -B "$branch" --track "origin/$branch"
            if ! git rebase upstream/v0.6; then
                echo "failed, skipping"
                continue
            fi
            echo "success, pushing"
            git push --force origin -u "$branch:$branch"
        else
            echo "up to date"
        fi
    done
    rm -f "$pulljs"
}

function push_upstream
{
    git push upstream -u upstream-v0.6:v0.6
}

case "${1}" in
    "mergepullrequest")
	if [ -z "${2}" ]; then
	    echo "No PR# specified, here is a list:"
	    curl -s https://api.github.com/repos/Bitmessage/PyBitmessage/pulls -s | jq '.[] | .number, .title' | paste - -
	    exit 1
	fi
        mergepullrequest "${2}"
	;;
    "importgpgkey")
	if [ -z "${2}" ]; then
	    echo "No username specified, here is a list from recent PRs:"
	    curl -s https://api.github.com/repos/Bitmessage/PyBitmessage/pulls -s | jq '.[].user.login' | sort -u
	    exit 1
	fi
        import_gpg_key "${2}"
	;;
    "rebase")
        rebase_open_prs
        ;;
    "pushupstream")
        push_upstream
        ;;
esac
