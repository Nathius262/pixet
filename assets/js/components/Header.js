function Header(){
    let el = `
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarsWow" aria-controls="navbarsWow" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="container">
            <!-- Begin Logo -->
            <a class="navbar-brand" href="index.html">
                <img src="assets/images/logo2.png" width="250" alt="PIXTINFINITY lOGO">
            </a>
            <!-- End Logo -->
            <!-- Begin Menu -->
            <div class="collapse navbar-collapse" id="navbarsWow">
                <!-- Begin Menu -->
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="index.html">Home</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Category</a>
                        <div class="dropdown-menu" aria-labelledby="dropdown01">
                            <a class="dropdown-item" href="category.html">News</a>
                        </div>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="blog.html">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="about.html">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="contact.html">Contact</a>
                    </li>
                    <li class="nav-item">
                        <a target="" class="nav-link highlight" href="#">Login</a>
                    </li>
                </ul>
                <!-- End Menu -->
            </div>
        </div>

    `

    return el
}


export {Header}