NodeHub
=======

NodeHub is a datacenter management tool.

### Requirements

* [Python](http://www.python.org/) >= 2.6
* [Django](https://www.djangoproject.com/) >= 1.3
* [ipaddr](http://code.google.com/p/ipaddr-py/)

## Development (setup)
 
    # Setup Python environment
    virtualenv dev

    # Activate environment
    source dev/bin/activate

    # Install dependencies
    pip install --upgrade django ipaddr

    # Create database
    python nodehub/manage.py syncdb

## Development (run)

    # Activate environment
    source dev/bin/activate

    # Run development server
    python nodehub/manage.py runserver

### License

This work is licensed under the MIT License (see the LICENSE file).
