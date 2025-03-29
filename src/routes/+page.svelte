<h1>Blog</h1>
<h2>by Minerva_Juppiter</h2>
<br/>
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