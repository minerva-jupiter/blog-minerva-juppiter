<h3>Articles</h3>
<ul>
    {#each articles as article,index}
        <a href="./article/{index}">
            <li>{article.ArticleName}</li>
        </a>
    {/each}
</ul>

<script lang="ts">
    import articles from "$lib/assets/articles.json";
</script>

<style>
    h3 {
        color: whitesmoke;
        padding-left: 3rem;
    }
    ul {
        padding-left: 3rem;
    }
    a {
        text-decoration: none;
        color: white;
    }
</style>