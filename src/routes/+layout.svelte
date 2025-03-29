<header>
    <h1>Blog</h1>
    <h2>by Minerva_Juppiter</h2>
    <nav>
        <a href="/">Home</a>
        /
        <a href="/about">About</a>
    </nav>
</header>
<br/>
<slot />
<br/>
<footer>
    <p>
        @all right reserved by Minerva_Juppiter
    </p>
</footer>

<style>
    :global(body) {
        background-color: black;
        color: whitesmoke;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    header {
        background-color: #c2c2c2;
        color: #0f0a05;
        padding: 2rem;
    }
    nav a {
        text-decoration: none;
        color: black;
    }
    footer {
        background-color: #0f0a05;
        color: gray;
        padding: 1rem;
    }
</style>