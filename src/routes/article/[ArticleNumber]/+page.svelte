<script lang="ts">
    import type { PageProps } from './$types';
    import articles from '$lib/assets/articles.json';

    let { data }: PageProps = $props();
</script>

<h1>{articles[data.content].ArticleName}</h1>

<p>{articles[data.content].ArticleBody}</p>