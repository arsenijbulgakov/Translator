def task_html():
    """Make HTML documentation."""
    return {
            'actions': ['make -C docs html']
           }


def task_extract():
    """Create `.pot` file."""
    return {
            'actions': ['pybabel extract . -o msg.pot'],
            'targets': ['msg.pot'],
           }


def task_update():
    """Update translations."""
    return {
            'actions': ['pybabel update --ignore-pot-creation-date -D msg '
                        + '-i msg.pot -l ru_RU.UTF-8 -d po'],
            'file_dep': ['msg.pot'],
            'targets': ['po/ru_RU.UTF-8/LC_MESSAGES/msg.po'],
           }


def task_compile():
    """Compile translations."""
    return {
            'actions': [
                'pybabel compile -D msg -i po/ru_RU.UTF-8/LC_MESSAGES/msg.po -l ru_RU.UTF-8 -d po'
                       ],
            'file_dep': ['po/ru_RU.UTF-8/LC_MESSAGES/msg.po'],
            'targets': ['po/ru_RU.UTF-8/LC_MESSAGES/msg.mo'],
           }


def task_flake8():
    """Check with flake8."""
    return {
        'actions': ['flake8 .'],
        }


def task_isort():
    """Check with isort."""
    return {
        'actions': ['isort --check .'],
        }


def task_pydocstyle():
    """Check with pydocstyle."""
    return {
        'actions': ['pydocstyle .'],
        }


def task_test():
    """Perform tests."""
    return {
        'actions': ['pytest -v test.py'],
        }
