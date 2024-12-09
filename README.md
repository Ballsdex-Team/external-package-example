# Ballsdex - 3rd party package example

This repo serves as an example on how to write and share custom packages for
Ballsdex, without having to edit source code other than the `config.yml`
file (in theory).

It contains one package named `example_package`, which itself contains
one command `/randomball` returning a random countryball from the player's
inventory.

## How to install

There are multiple ways to install an external package depending on your
configuration. I am aware this installation process is not easy, and
I'm open for suggestions on how to do it better.

### If you're using Docker

Edit the file `Dockerfile` and add this line:

```diff
  COPY . /code
  RUN mkdir -p /code/static
  RUN mkdir -p /code/static/uploads

+ RUN pip install --upgrade --force-reinstall git+https://github.com/Ballsdex-Team/external-package-example.git

  # wait for postgres to be ready
  CMD sleep 2
```

Then run `docker compose build` before running the usual commands.

### If you're not using Docker

Run the command `poetry add -n git+https://github.com/Ballsdex-Team/external-package-example.git`

----

Then, open `config.yml`, look for the key that's named `packages` and
add the package:

```diff
  # list of packages that will be loaded
  packages:
    - ballsdex.packages.admin
    - ballsdex.packages.balls
    - ballsdex.packages.config
    - ballsdex.packages.countryballs
    - ballsdex.packages.info
    - ballsdex.packages.players
    - ballsdex.packages.trade
+   - example_package
```

## How to publish your own packages

If you have packages that you wish to publish and follow
the recommended way of Ballsdex, here's the process:

1. Create a git repository (Github, Gitlab or any other platform)
2. Create a LICENSE that will cover your code. If you don't know which license to pick, MIT is a simple permissive one, used by Ballsdex.
3. Create a `pyproject.toml` file. You can use the one in this repository as an example (**change the author and package name**) or follow [this guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
4. Upload the files of your package in a folder like this:
   ```
   LICENSE
   pyproject.toml
   package_name
   ├── __init__.py
   ├── cog.py
   └── ...
   ```
   If you have multiple packages that you wish to publish in the same repository, follow this structure instead:
   ```
   LICENSE
   pyproject.toml
   collection_name
   ├── package_one
   │   ├── __init__.py
   │   ├── cog.py
   │   └── ...
   └── package_two
       ├── __init__.py
       ├── cog.py
       └── ...
   ```

That's it! Remember to change the `name` in `pyproject.toml` to the name of your main folder.

[!WARNING]
> If you change some code, you should change the version number in `pyproject.toml`, otherwise pip won't notice a change in code.
