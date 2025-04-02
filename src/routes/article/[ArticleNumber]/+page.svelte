<script lang="ts">
    import type { PageProps } from './$types';
    import articles from '$lib/assets/articles.json';

    let { data }: PageProps = $props();


</script>

<div>
    <h1>{articles[data.content].ArticleName}</h1>

    <h4>{articles[data.content].Date}</h4>

    <pre>{articles[data.content].ArticleBody}</pre>
</div>

<style>
    div {
        padding-left: 4rem;
        padding-right: 4rem;
    }
    pre {
        font-family: "Tw Cen MT","Century Gothic","Noto Sans JP";
        white-space: pre-wrap;
    }
</style>

<svelte:head>
    <title>
        {articles[data.content].ArticleName}
    </title>
</svelte:head>