const endpoint = "https://pixtinfinity.pythonanywhere.com"
const blog_endpoint = endpoint+"/api/post/"
const tag_endpoint = endpoint+"/api/tag/"

async function fetchData(url, options) {
    const response = await fetch(url, options);
    const data = await response.json();
    return data;
}

async function navigateToDetailedPost() {
    const urlParams = new URLSearchParams(window.location.search);
    const post_url = `${blog_endpoint}${urlParams.get('post')}`;
    const data = await fetchData(post_url);
    //get element
    let postEl = document.querySelector('.article-post')
    let posttitleEl = document.querySelector('.posttitle')
    let tagEl = document.querySelector('.tags')
    let postimageEl = document.getElementById('postimage')
    //assign element from data
    posttitleEl.innerHTML = data.title
    postEl.innerHTML = data.body

    //tags
    for(let tag of data.tag){
        tagEl.insertAdjacentHTML('afterbegin', `
        <li>
            <a href="category?tag=${tag.id}">${tag.name}</a>
        </li>
    `)
    }
	news(tag_endpoint+data.tag[2].id)

    postimageEl.innerHTML = `<img class="featured-image img-fluid" src="${data.image}" alt="">`
}

async function renderModelList(url, options) {
    const data = await fetchData(url, options);
    // Render your model data here
    let itemElement = document.querySelector('.listrecent');
    const paginationContainer = document.getElementById('pagination');
    try {
        itemElement.innerHTML = '';
    } catch (TypeError) {
        
    }
    data.results.forEach(blog => {
        
        let el = `
            <!-- begin post -->
            <div class="col-md-6 grid-item">
                <div class="card">
                    <a href="blog?post=${blog.slug}">
                    <img class="img-fluid" src="${blog.image}" alt="${blog.title}">
                    </a>
                    <div class="card-block">
                        <h2 class="card-title"><a href="blog_detail?post=${blog.slug}">${blog.title}</a></h2>
                        <h4 class="card-text">
                        ${truncateWords(blog.body, 10)}
                        </h4>
                        <div class="metafooter">
                            <div class="wrapfooter">
                                <span class="meta-footer-thumb">
                                <!--<img class="author-thumb" src="" alt="pixitinfinity">-->
                                </span>
                                <span class="author-meta">
                                <span class="post-name"><a target="_blank" href="#">Pixtinfinity</a></span><br/>
                                <span class="post-date"></span>
                                </span>
                                <span class="post-read-more"><a href="blog_detail?post=${blog.slug}" title="Read Story"><i class="fa fa-link"></i></a></span>
                                <div class="clearfix">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- end post -->
        `

        itemElement.insertAdjacentHTML('afterbegin', el)

    });

    // Render pagination links
    paginationContainer.innerHTML = '';

    if (data.previous) {
        paginationContainer.innerHTML += `
            <li class="page-item">
                <a class="page-link" href="${data.previous}">&laquo; Previous</a>
            </li>
        `
    }

    //stepLinks.innerHTML += `<span class="current">Page ${data.current_page} of ${data.num_pages}.</span>`;

    if (data.next) {

        paginationContainer.innerHTML += `
            <li class="page-item">
                <a class="page-link" href="${data.next}">Next</a>
            </li>
        `
    }
    
    

}

function truncateWords(text, limit) {
    const words = text.split(' ');
    if (words.length > limit) {
        return words.slice(0, limit).join(' ') + '...';
    }
    return text;
}


async function news(url, options){
    let newsEl = document.querySelector('#main-news')
    let el
    const data = await fetchData(url, options);
    data.results.forEach(blog => {

        el = `
            <div class="col-md-4">
                <div class="mn-img">
                    <img src="${blog.image}">
                    <div class="mn-title">
                        <a href="blog_detail?post=${blog.slug}" data-locate="${blog.abssolute_url}" class="locate-data">${blog.title}</a>
                    </div>
                </div>
            </div>
        `

        try {
            newsEl.insertAdjacentHTML('afterbegin', el)
        } catch (TypeError) {
            
        }
    })

}

async function tagPostList() {
    const tag_url = `${endpoint}/api/tag/`;
    const data = await fetchData(tag_url);
    let tagListEl = document.querySelector('.tag_list')
    let readmoretagEl = document.querySelector('.read-more')
    data.results.forEach(blog => {
        tagListEl.insertAdjacentHTML('afterbegin', `
            <a class="dropdown-item" href="category?tag=${blog.id}">${blog.name}</a>
        `)
        readmoretagEl.insertAdjacentHTML('afterbegin', `
            <li><a href="category?tag=${blog.id}">${blog.name}</a></li>
        `)
    })
}

async function tagPostFilterList() {
    const urlParams = new URLSearchParams(window.location.search);
    const post_url = `${tag_endpoint}${urlParams.get('tag')}`;
    const data = await fetchData(post_url);
    // Render your model data here
    let itemElement = document.querySelector('.listrecent');
    const paginationContainer = document.getElementById('pagination');
    const tagEl = document.querySelector('.tag-title')
    try {
        itemElement.innerHTML = '';
    } catch (TypeError) {
        
    }
    data.results.forEach(blog => {
        
        let el = `
            <!-- begin post -->
            <div class="col-md-6 grid-item">
                <div class="card">
                    <a href="blog?post=${blog.slug}">
                    <img class="img-fluid" src="${blog.image}" alt="${blog.title}">
                    </a>
                    <div class="card-block">
                        <h2 class="card-title"><a href="blog_detail?post=${blog.slug}">${blog.title}</a></h2>
                        <h4 class="card-text">
                        ${truncateWords(blog.body, 10)}
                        </h4>
                        <div class="metafooter">
                            <div class="wrapfooter">
                                <span class="meta-footer-thumb">
                                <!--<img class="author-thumb" src="" alt="pixitinfinity">-->
                                </span>
                                <span class="author-meta">
                                <span class="post-name"><a target="_blank" href="#">Pixtinfinity</a></span><br/>
                                <span class="post-date"></span>
                                </span>
                                <span class="post-read-more"><a href="blog_detail?post=${blog.slug}" title="Read Story"><i class="fa fa-link"></i></a></span>
                                <div class="clearfix">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- end post -->
        `

        itemElement.insertAdjacentHTML('afterbegin', el)

    });

    // Render pagination links
    paginationContainer.innerHTML = '';

    if (data.previous) {
        paginationContainer.innerHTML += `
            <li class="page-item">
                <a class="page-link" href="${data.previous}">&laquo; Previous</a>
            </li>
        `
    }

    //stepLinks.innerHTML += `<span class="current">Page ${data.current_page} of ${data.num_pages}.</span>`;

    if (data.next) {

        paginationContainer.innerHTML += `
            <li class="page-item">
                <a class="page-link" href="${data.next}">Next</a>
            </li>
        `
    }
    
    

}

function errorMessage(error_message){            
    let createSquadForm = `
        <div class="modal fade" id="error-message" tabindex="-1" aria-labelledby="errorMessageTitle" style="display: none;" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
            <div class="modal-header">
            <h5 class="modal-title" id="errorMessageTitle">Create Team</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <p class="text-danger">${error_message}</p>
                
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
        </div>
        </div>
        </div>
    `

    document.body.insertAdjacentHTML('beforebegin', createSquadForm) 
    $('#error-message').modal('show');
}

export{renderModelList, errorMessage, tagPostList, tagPostFilterList, news, navigateToDetailedPost}