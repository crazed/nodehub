NodeHub
=======

NodeHub is a datacenter management tool.

## Development
 
    # Setup Python env
    virtualenv dev

    # Activate env
    source dev/bin/activate

    # Install deps
    pip install -Ur requirements.txt

    # Set Django env
    export DJANGO_ENV=dev

    # Sync database
    python nodehub/manage.py syncdb

    # Run development server
    python nodehub/manage.py runserver

### License

This work is licensed under the MIT License (see the LICENSE file).
