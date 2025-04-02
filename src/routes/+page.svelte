<h1>Articles</h1>
<ul>
    {#each articles as article,index}
        <li>
            <a href="./article/{index}">
                {article.ArticleName}
            </a>
        </li>
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
        padding-top: 0rem;
        padding-left: 4rem;
        font-size: large;
    }
    li {
        padding: 0.5rem;
    }
    a {
        text-decoration: none;
        color: #d9d9d9;
    }
</style>

<svelte:head>
    <title>Blog Minerva_Juppiter</title>
</svelte:head>