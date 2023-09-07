<h1 align="center">Favorite Movies</h1>
<h3 align="center"><a href="https://bookshelf.applikuapp.com">movies.applikuapp.com</a></h3>

<br/>

<br/>

<h2>About this Project</h2>
<p>The genesis of this project stemmed from my desire to showcase my preferred movies on the web, as I firmly believe that one's choice of entertainment offers valuable insights into their personality. This motivation led to the creation of this movie showcase, complementing my Bookshelf application. Both of these endeavors were undertaken with the overarching objective of honing my skills in developing comprehensive, full-stack web applications.</p>

<p>The backend is crafted using Python, Flask, and Flask accessories. In addition to Python and it's modules, this application harnesses the power of a The Movie Database (TMDB) API to fetch essential details such as movie titles, release dates, summaries, and posters. The toolkit employed in crafting this application encompasses:
<ul>
  <li>Python</li>
  <li>Flask</li>
  <li>Flask-SQLAlchemy</li>
  <li>TMDB API</li>
  <li>JavaScript</li>
  <li>HTML</li>
  <li>CSS</li>
  <li>Boostrap</li>
</ul>
</p>
<h3>Front End:</h3>
<p>Creating the frontend of this website posed an interesting challenge. Each movie is presented as a card, automatically arranged in ascending order of rank. On the front face of these cards, you'll find the movie poster, with the rank prominently displayed at the center. A interactive feature is triggered when you hover your mouse over any card—each card flips over to reveal additional details, including the rating, personal comments, and a concise movie summary.</p>

<p>For added control, users can edit or remove movies from their collection, provided they possess the secret code to access these actions. It's noteworthy that all of these dynamic visual effects were achieved using pure CSS, with Bootstrap being employed sparingly, only when necessary.</p>

<p>The search functionality, on the other hand, relies on the <b>TMDB API</b> to perform searches. It returns a list of movies matching the user's query, presenting them with release dates and posters (visible when users hover over titles). This interface allows users to select a movie, assign a rating, provide comments, and seamlessly add it to their list. The heavy lifting for the rest of the operations is handled by the backend, ensuring a smooth user experience.</p>

<h3>Back End:</h3>
<p>The backend of the project was predominantly built using <b>Python</b> alongside the <b>Flask</b> framework, chosen for its simplicity and suitability for smaller projects. <b>Flask-SQLAlchemy</b> was employed for efficient database management and queries, and the <b>TMDB API</b> played a crucial role in fetching movie data. To present this information elegantly on the client side, I employed <b>Jinja</b> as the templating engine. In the end, the backend proved to be a well-crafted fusion of <b>Python, Flask, Flask-SQLAlchemy, TMDB API, and Jinja</b>, working together seamlessly to deliver a feature-rich and user-friendly experience.</p>





