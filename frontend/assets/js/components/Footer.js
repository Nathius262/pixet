let date = new Date()
date = date.getFullYear()

function footer(){
    let el = `
    <div class="container">
            <div class="row">
                <div class="col-sm-3">
                    <div class="footer-widget">
                        <a href="contact.html">
                        <img src="assets/images/logo-footer.png" alt="logo footer">
                        </a>
                    </div>
                </div>
                <div class="col-sm-3">
                    <div class="footer-widget">
                        <h5 class="title">Resources</h5>
                        <ul>
                            <li><a target="_blank" href="#">Digital Ocean</a></li>
                            <li><a target="_blank" href="#">GitHub</a></li>
                            <li><a target="_blank" href="#">Cloudinary</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-sm-3">
                    <div class="footer-widget">
                        <h5 class="title">Author</h5>
                        <ul>
                            <li><a href="/frontend/about.html">About Us</a></li>
                            <li><a href="/blog_list/">Blog</a></li>
                            <li><a href="/contact/">Contact</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-sm-3 text-primary text-right footersocial">
                    <p class="h5">Connect with Us</p>
                    <i class="fa fa-facebook"></i>
                    <i class="fa fa-twitter"></i>
                    <i class="fa fa-google"></i>
                    <i class="fa fa-pinterest"></i>
                    <i class="fa fa-github"></i>
                </div>
            </div>
            <div class="copyright">
                <p class="pull-left">
                    Copyright © ${date} PIXTINFINITY
                </p>
                <p class="pull-right">
                    <!-- Leave credit to author unless you own a commercial license: https://www.wowthemes.net/freebies-license/ -->
                    <a href="https://www.wowthemes.net/affiliates-free-bootstrap-template/">"Powered by"</a> - Infinity
                </p>
                <div class="clearfix">
                </div>
            </div>
        </div>
    `
    return el
}

export {footer}