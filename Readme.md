### How to get this project to run on first time
---

#### <b>Backend Part</b>:
1. Change directory to the `backend` folder by running command `cd backend`.
2. Create a virtul environment for python by run command `python -m venv {{name of venv here}}`.
3. Install all the required packages by running command `pip install -r requirements.txt`.
4. Run the command `pip install -e .` to install the backend folder as a package.
5. Run the command `python app.py` to start the backend server.

<br>

#### <b>Frontend Part</b>:
1. Change directory to the `frontend` folder by running command `cd frontend`.
2. Install all the required packages by running command `npm install`.
3. Run the command `npm run dev` to start the frontend server in development mode or `npm run preview` for production mode.

<br>

### Tech Stacks of this project
---
- Flask: Backend framework to develop API
- APIFlask: A simple wrapper of Flask with additional features like Marshmellow, OpenAPI, etc.
- Sqlalchemy: ORM to interact with database
- SQLite: A single file database
- Whoosh: Full text search engine
- Flask-Migrate: To manage migration of database
- flask-jwt-extended: To manage JWT token for authentication
- Sveltekit: Frontend framework to develop website
- svelte-carousel: A carousel library for svelte / sveletekit
- sveltekit-flash-message: A flash message library for svelte / sveltekit

<br>

### Flask shell
---
- Flask come with it's own shell to interact with the application. To start the shell, run the command `flask shell` in the terminal.
- You can register your own shell command inside the `make_shell_context` function in the `app.py` file.

<br>

### Flask Migrate
---
- Whenever you making change about the `models.py`, you are necessary to run the command `flask db migrate -m {{migrate message}}` to generate the migration file and then run the command `flask db upgrade` to apply the migration to the database.
- Think of flask migrate as a version control for database.
- A tricky approach to delete all data but keep the model defined is by running the combination of commands `flask db downgrade base` followed by `flask db upgrade`.

<br>

### Color Schemes
---
- #d09fdc light purple
- #FFB6C1 light pink
- #AEE0FF baby blue

<br>

### References
---

<br>

##### SQLALCHEMY
---
1. [Flask-sqlalchemy Pagination](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination)

2. [How to turn Flask SQLAlchemy query results into JSON for an API?](https://www.reddit.com/r/flask/comments/vll4xu/af_how_to_turn_flask_sqlalchemy_query_results/)

3. [Define relationship in Sqlalchemy](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)

4. [Real Python Data Management With Python, SQLite, and SQLAlchemy](https://realpython.com/python-sqlite-sqlalchemy/#working-with-sqlalchemy-and-python-objects)

5. [What's New in Sqlalchmemy 2.0](https://blog.miguelgrinberg.com/post/what-s-new-in-sqlalchemy-2-0)

<br>

#### Flask
---
1. [Handle image between flask to frontend](https://github.com/Vuka951/tutorial-code/blob/master/flask-file-upload/done/app.py)

2. [Handle image between flask to frontend by encode image into base64](https://www.quora.com/How-do-you-insert-an-image-into-a-database-using-Python-and-Flask)

3. [Maybe way to store image in flask backend](https://imagekit.io/blog/image-sharing-app-with-python/)

4. [Walle - A very pro example of flask application](https://github.com/meolu/walle-web/tree/master)

5. [Example application based on the tutorial "Flask Mega Tutorial Series"](https://github.com/miguelgrinberg/microblog/tree/v0.23)

6. [How to build an image-sharing app with Flask and ImageKit](https://imagekit.io/blog/image-sharing-app-with-python/)

<br>

#### Sveltekit / Svelte
---
1. [Global styles in sveltekit](https://joyofcode.xyz/global-styles-in-sveltekit)

2. [Horizontal scroll of list of brand](https://medium.com/@mintpw/how-to-create-infinite-horizontal-scroll-and-hover-pause-with-pure-css-b052caa683bd)

3. [Svelte Carousel](https://vadimkorr.github.io/svelte-carousel/)

4. [Create accordia in Svelte](https://svelte.dev/repl/29bf8248d5044e12877e9cbec9381115?version=3.48.0)

5. [Using local storage in Svelte with Svelte store](https://rodneylab.com/using-local-storage-sveltekit/)

6. [Sveltekit form action](https://kit.svelte.dev/docs/form-actions)

7. [Form action example in sveltekit with Post HTTP request](https://sveltebyexample.com/form-actions/)

8. [Settings cookie from header in svelte by using 'set-cookie-parser' package](https://github.com/sveltejs/kit/issues/8409)

9. [Create button group in svelte](https://svelte.dev/repl/7dae7f254a2348d5ad42ad09d84a137f?version=3.24.1)

10. [Official Sveltekit implementation of real world app](https://github.com/sveltejs/realworld)

11. [SvelteKit Authentication Using Cookies](https://joyofcode.xyz/sveltekit-authentication-using-cookies)

12. [Protecting sveltekit routes from unauthenticated users](https://dev.to/thiteago/protecting-sveltekit-routes-from-unauthenticated-users-nb9)

13. [sveltekit-flash-message](https://github.com/ciscoheat/sveltekit-flash-message)

<br>

#### Full Text Search
---
1. [Full Text Search with Whoosh-Reloaded](https://sygil-dev.github.io/whoosh-reloaded/)

2. [Example to integreate whoosh into flask sqlalchemy](https://github.com/Momo8289/Flask-SQLAlchemy-Whoosh)

3. [Full Text Search using Elasticsearch](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-full-text-search)

#### Others
---
1. Dataset Source: 
[Fashion Product Images Dataset](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset)

2. [Youtube Sample Design](https://www.youtube.com/watch?v=gQlLw4cmq_o)

3. [Resolving intra-project imports in Python — A simple guide](https://fadil-nohur.medium.com/resolving-intra-project-imports-in-python-a-simple-guide-872775f64277)

4. [Resolving intra project imports in python a simple guide visual studio code](https://fadil-nohur.medium.com/resolving-intra-project-imports-in-python-a-simple-guide-visual-studio-code-98472b0a8f59)

5. [Free SVG Icons](https://www.svgrepo.com/)

6. [A Design Pattern for Python API Client Libraries](https://bhomnick.net/design-pattern-python-api-client/)

7. [Simple Alert/Notification Design](https://codepen.io/kkundi/pen/BoaYrK)