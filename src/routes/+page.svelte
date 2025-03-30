<h1>Articles</h1>
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
    h1 {
        padding-left: 4rem;
    }
    ul {
        padding-left: 4rem;
        font-size: large;
    }
    a {
        text-decoration: none;
        padding: 4rem;
        color: #d9d9d9;
    }
</style>

<svelte:head>
    <title>Blog Minerva_Juppiter</title>
</svelte:head>