<script lang="ts">
    import type { PageProps } from './$types';
    import articles from '$lib/assets/articles.json';

    let { data }: PageProps = $props();
</script>

<div>
    <h1>{articles[data.content].ArticleName}</h1>

    <h4>{articles[data.content].Date}</h4>

    <p>{articles[data.content].ArticleBody}</p>
</div>

<style>
    div {
        padding-left: 4rem;
        padding-right: 4rem;
    }
</style>