# Accessing files with `git stash`

To access files with `git stash`, there are a few options, depending on what you want to do:

1. `git stash list`: lists all the stashes that you have created. Each stash is identified by a unique name such as `stash@{0}`, `stash@{1}`, etc. The most recent stash is usually `stash@{0}`.
2. `git stash show`: displays the changes that were stashed. By default, it shows the changes in the most recent stash (`stash@{0}`), but you can specify a different stash name as an argument to view changes in other stashes.
3. `git stash branch <branchname>`: creates a new branch and applies the changes from the most recent stash to the new branch. It is useful when you want to create a new branch to work on the stashed changes.
4. `git stash apply <stashname>`: applies the changes from a specific stash to your current branch without removing the stash. You need to specify the stash name as an argument. For example: `git stash apply stash@{1}`.
5. `git stash pop <stashname>`: applies the changes from a specific stash to your current branch and removes the stash. You need to specify the stash name as an argument. For example: `git stash pop stash@{1}`.
6. `git stash drop <stashname>`: removes a specific stash without applying its changes. You need to specify the stash name as an argument. For example: `git stash drop stash@{1}`.
7. `git stash branch <branchname> <stashname>`: creates a new branch from the current branch and applies the changes from a specific stash to the new branch. It is useful when you want to create a new branch and apply stashed changes in a single command.
