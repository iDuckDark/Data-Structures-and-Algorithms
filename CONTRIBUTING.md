# Contributing
Thank you for considering contributing. Due to the relatively simple nature of the project, the main focus is on code quality and exposition. It's a great project for your first contribution.

## Appreciated Contributions
- Adding a new algorithm or data structure implementation
- Improving an existing algorithm or data structure
    - Better implementation (fewer loc, less complexity, etc.)
    - Using more appropriate variable names
- Improving problem and alogorithm descriptions
- Reorganizing algorithms into more appropriate locations


## Reporting Issues
Report bugs using the [issue tracker](https://github.com/benburk/dsa_python/issues). If an algorithm or data structure isn't working as expected, include the test case.

## Contributing
1. Fork the repository
2. install pre-commit (`pip install pre-commit`) to ensure style-guides and code checks are followed.
3. Run `pre-commit install`
3. `git checkout -b <branch-name>`
4. Edit, add, and commit your changes.
5. `git push -u origin <branch-name>`
6. Navigate to the branch on github. Click compare & pull request
7. Add your message, then click create pull request

## Adding something
- pick an algorithm
- pick a category
- name the file
- `dsa/category/file_name.py`
- import * into `__init__.py`
- add test to `tests/test_category.py`
