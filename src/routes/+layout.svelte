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
        color: #d9d9d9;
        font-family: "Tw Cen MT","Century Gothic","Noto Sans JP";
    }
    header {
        background-color: #d9d9d9;
        color: #0f0a05;
        padding-left: 4rem;
        padding-right: 4rem;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    nav a {
        text-decoration: none;
        color: black;
        font-size: large;
    }
    footer {
        background-color: #0f0a05;
        text-align: center;
        color: gray;
        padding: 1rem;
    }
</style>