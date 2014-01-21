capysule
========

Python bindings for the Capsule API, with a synchronous
[Requests][]-based client modeled on [Finch][], using the
data-modeling and validation framework [Booby][].

Development
-----------

Create .env with `CAPSULE_SITE` and `CAPSULE_API_TOKEN`

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements_dev.txt
    foreman run capysule/test.py


[Requests]: http://docs.python-requests.org/en/latest/
[Finch]: https://github.com/jaimegildesagredo/finch
[Booby]: https://booby.readthedocs.org/en/0.5.0/
