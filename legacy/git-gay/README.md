# git-gay

- git checkout HEAD^: 바로 이전 commit으로 이동. relative refs.
- git branch -f master HEAD~3: Moves (by force) the master branch to three parents behind HEAD.
- There are two primary ways to undo changes in Git -- one is using `git reset` and the other is using `git revert`.
- `git reset HEAD^`: 바로 전으로 돌아가는 것이고. (현재 커밋 스냅샷을 버리고)
- `git revert HEAD^`: 바로 전 커밋을 커밋 스냅샷으로 이용
- `git merge bugFix`: 현재 branch 에 merge.
- `git rebase -i HEAD~4 --aboveAll`
- `git rebase master`: bugFix 브랜치에 기준이 있고, master 다음 가지로 commit 스냅샷을 옮깁니다.

![](https://www.dropbox.com/s/v8wnby0amzu6xww/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-01-22%2010.12.59.png?raw=1)

- `git reset HEAD~1`: HEAD로 부터 하나 전으로 reset.
