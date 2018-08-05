let searchField = $('#search-field');
let initialArticle = $('.initial-article');
let allArticles = $('.all-articles');
let delayTimer;

marked.setOptions({
    sanitize: true,
    baseUrl: "../"
});

searchField.on('input', () => {
    let query = searchField.val().toLowerCase();
    if (query.length > 1 || (!isNaN(query) && query.length > 0)) {
        clearTimeout(delayTimer);
        delayTimer = setTimeout(function () {
            ajaxSearch(query);
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

    if (introduction.toLowerCase().includes(query)) {
        [indexStart, indexEnd] = highlight(introduction.toLowerCase(), query);
        console.log(indexStart, indexEnd);
        introduction = introduction.substring(0, indexStart) + '<span class="highlight">' + introduction.substring(indexStart, indexEnd) + '</span>' + introduction.substring(indexEnd);
        bodyText = "";
    }
    else {
        introduction = "";
        let bodyTextLower = bodyText.toLowerCase();
        let bodyTextArray = bodyTextLower.split(/\.|\||,/);
        let matchArray = [];
        for (let i = 0; matchArray.length < 2 && i < bodyTextArray.length; i++) {
            if (bodyTextArray[i].includes(query)) {
                [indexStart, indexEnd] = highlight(bodyTextArray[i].toLowerCase(), query);
                console.log(indexStart, indexEnd);
                matchArray.push(bodyTextArray[i].substring(0, indexStart) + '<span class="highlight">' + bodyTextArray[i].substring(indexStart, indexEnd) + '</span>' + bodyTextArray[i].substring(indexEnd));
            }
        }
        bodyText = "";
        for (let i in matchArray) {
            bodyText += "..." + matchArray[i] + "...<br><br>";
        }

    }
    return [introduction, bodyText];
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
            // trimmedText = trimBodyText(articles[key].body_text, articles[key].introduction, query);
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