let searchField = $('#search-field');
let initialArticle = $('.initial-article');
let allArticles = $('.all-articles');
let delayTimer;

marked.setOptions({
    sanitize: true,
    baseUrl: "../"
});

searchField.on('input', () => {
    let query = searchField.val();
    if (query.length > 1 || (!isNaN(query) && query.length > 0)) {
        clearTimeout(delayTimer);
        delayTimer = setTimeout(function () {
            var t0 = performance.now();
            ajaxSearch(query);
            var t1 = performance.now();
            console.log("Call to doSomething took " + (t1 - t0) + " milliseconds.")
        }, 800); // Sends the query to the server after it's been 800ms idle
    } else {
        searchResult("");
    }
});

function addArticleBox(target, title, introduction, bodyText, slug) {
    let articleHTML =
        '<a href="/wiki/' + slug + '" class="article-preview resize search-result">' +
        '<h4>' + title + '</h4>';

    if (introduction.length > 0) {
        articleHTML += '<p class="article-introduction">' + introduction + '</p>';
    }
    if (bodyText.length > 0) {
        articleHTML += '<p class="article-body-text">' + bodyText + '</p>';
    }

    articleHTML += '</a>';

    target.append(articleHTML);
}

function highlight(result, query) {
    indexStart = result.indexOf(query);
    indexEnd = indexStart + query.length;
    return [indexStart, indexEnd];
}

function trimBodyText(bodyText, introduction, query) {
    let isWithQuery;
    let introductionIncludes = false;
    if (introduction) {
        introduction = introduction.toLowerCase();
        if (introduction.includes(query.toLowerCase())) {
            introductionIncludes = true;
        }
    }

    // Return body-text only if introduction doesn't contain query
    if (!introductionIncludes) {
        // Don't return the introduction
        introduction = "";

        isWithQuery = [];
        // Splits on . for sentences and | for tables
        let bodyArray = bodyText.split(/\.|\||,/);

        // Loops through all sentences to see which ones contains the query
        for (let i in bodyArray) {
            if (bodyArray[i].toLowerCase().includes(query.toLowerCase())) {
                // Highlight adds a <span class"highlight"> around the query in the text
                [indexStart, indextEnd] = highlight(bodyArray[i], query);
                let tempText = bodyArray[i].substring(0, indexStart) + '<span class="highlight">' + bodyArray[i].substring(indexStart, indexEnd) + '</span>' + bodyArray[i].substring(indexEnd);
                // Adds the sentence containing query to isWithQuery array
                isWithQuery.push(tempText);
                // Break if more than 2 sentences contains query
                if (isWithQuery.length > 1) {
                    break;
                }
            }
        }
        // Construct string
        bodyText = "";
        for (let i in isWithQuery) {
            bodyText += "..." + isWithQuery[i] + "...<br><br>";
        }
    // Introduction contains query. Don't return the body-text
    } else {
        bodyText = "";
        [indexStart, indextEnd] = highlight(introduction, query);
        introduction = introduction.substring(0, indexStart) + '<span class="highlight">' + introduction.substring(indexStart, indexEnd) + '</span>' + introduction.substring(indexEnd);
    }
    return [bodyText, introduction];
}

function searchResult(articles, query) {
    let trimmedText;
    $('.search-result').remove();
    // If no results:
    if (articles.length === 0) {
        initialArticle.show();
    } else {
        // Hides all articles
        initialArticle.hide();
        for (let key in articles) {
            // Removes the unnecessary body-text/introduction and adds highlight
            trimmedText = trimBodyText(articles[key].body_text, articles[key].introduction, query);
            // Adds the results to the wiki-page
            addArticleBox(allArticles, articles[key].title, trimmedText[1], trimmedText[0], articles[key].slug);
        }
    }
}

// Sending the search query to the server
function ajaxSearch(query) {
    $.ajax({
        type: 'GET',
        data: {
            'q': query,
        },
        success: function (data) {
            data = data;
            searchResult(data, query);
        },
        error: function (data) {
            console.log("Error");
        }
    });
}