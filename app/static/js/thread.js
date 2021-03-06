class Thread extends React.Component {
    constructor(p) {
        super(p);

        this.state = {
            thread: window.location.pathname.substring(1),
            posts: [],
            token: "",
            new_post: "",
        }
    }

    componentDidMount() {
        // Initializes thread posts and adds response data for each post and response
        fetch(window.location.origin + "/api/posts/" + this.state.thread)
        .then(response => response.json())
        .then(data => {
            data.posts.map(post => {
                post['respond_data'] = { 
                    display: "none", 
                    body: "",
                };
                post.responses.map(response => {
                    response['respond_data'] = { 
                        display: "none",
                        body: "",
                    };
                        });
                    });
            this.setState({posts: data.posts})
        })

        // Retrieves authentication token
        fetch(window.location.origin + "/api/tokens", {method: "POST", headers: {"Content-Type": "application/json"}})
        .then(response => response.json())
        .then(data => this.setState({token: data.token}));

    }

    respondToPost = (post) => {
        const data = post.respond_data;
        data.display = data.display == "none" ? "block" : "none";
        this.forceUpdate();
        var response_body = data.body.trim();
        if (response_body.length > 0) {
            const url = window.location.origin + "/api/post/" + post.id + "/respond";
            const request = {
                method: "POST",
                headers: { 
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + this.state.token},
                body: JSON.stringify({
                    body: response_body,
                    response_to_user_id: post.user_id,
                })};
            fetch(url, request).then(response => response.json()).then(data => {
                data['respond_data'] = { 
                    display: "none",
                    body: "",
                };
                post.responses.push(data);
                this.forceUpdate();
        });}
        data.body = "";
    }

    postComment = () => {
        const url = window.location.origin + "/api/post";
        const comment = this.state.new_post;
        const data = comment.trim();
        if (data.length > 0) {
            const request = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + this.state.token},
                body: JSON.stringify({
                    body: comment,
                    thread: this.state.thread
                })};
            fetch(url, request).then(response => response.json()).then(data => {
                data['respond_data'] = {
                    display: "none",
                    body: "",
                };
                this.state.posts.push(data);
                this.forceUpdate();
            });
            this.setState({new_post: ""});
        }
    }

    respondToResponse = (response, parent) => {
        const data = response.respond_data;
        
        data.display = data.display == "none" ? "block" : "none";
        this.forceUpdate();

        const response_body = data.body.trim();
        
        if (response_body.length > 0) {
            const url = window.location.origin + "/api/post/" + response.response_to_post_id + "/respond";
            const request = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + this.state.token},
                body: JSON.stringify({
                    body: response_body,
                    response_to_user_id: response.user_id,
                })};
            fetch(url, request).then(response => response.json()).then(data => {
                data['respond_data'] = {
                    display: "none",
                    body: "",
                };
            parent.responses.push(data);
            this.forceUpdate();
        });}
    }

    displayPosts = () => {
        const posts = this.state.posts
        if (posts.length == 0) {
            return(
                <div id="noPosts">
                    <h4>No Comments Yet</h4>
                    <p>Be the first one to share what you think!</p> 
                </div>)
        }

        return (
            <div>
                
                {posts.map((post) =>  
                    <div className="comment">
                        <img className="userpic" src={post.image}/>
                        <div className="text-box">
                            <h4 className="username" style={{color: post.color}}>{post.username}</h4>
                            <p>{post.body}</p>
                            <div className="responseinputcontainer"> 
                            <textarea className="responseinput" type="text" placeholder="Respond..." style={{display: post.respond_data.display}} onChange={e => {post.respond_data.body = e.target.value; this.forceUpdate()}} value={post.respond_data.body} onKeyDown={this.adjustInput}></textarea>
                            </div>
                            <div className="comment-interact">
                                <p className="numbers">{post.score}</p>
                                <i className="fas fa-light fa-chevron-up"></i>
                                <i className="fas fa-light fa-chevron-down"></i>
                                <p className="timer">{ moment(post.timestamp).fromNow()}</p>
                                <p className="respond" onClick={ () => this.respondToPost(post) }>Respond</p>
                            </div>
                        
                            {post.responses.map((response) =>
                                <div className="response-box">
                                <img className="responsepic" src={response.image}/>
                                <div className="response-text"> 
                                    <h5 className="username" style={{ color: response.color }}>{ response.username }</h5>
                                    <p><span className="at username">{ response.response_to_username }</span> { response.body }</p>
                                    <div className="responseinputcontainer"> 
                                    <textarea className="responseinput" type="text" placeholder="Respond..." style={{display: response.respond_data.display}} onChange={e => response.respond_data.body = e.target.value} onKeyDown={this.adjustInput}></textarea>
                                    </div>
                                    <div className="comment-interact">
                                        <p className="numbers">{ response.score }</p>
                                        <i className="fas fa-light fa-chevron-up"></i>
                                        <i className="fas fa-light fa-chevron-down"></i>
                                        <p className="timer">{ moment(response.timestamp).fromNow() }</p>
                                        <p className="respond" onClick={() => this.respondToResponse(response, post)}>Respond</p>
                                    </div>
                                </div>
                            </div>
                            
                            )}

                        </div>
                    </div>
                )}
            </div>)
    }

    adjustInput = (e) => {
        e.target.style.height = 'inherit';
        e.target.style.height = `${e.target.scrollHeight}px`;
    }

    render(){
        return (
            <div>
                
                <div id="place">
                    <input id="placebox" type="text" placeholder={this.state.thread}></input>
                </div>

                <div id="chatarea"> 
                    <div id="comments">
                        
                        <div id="comment_input">
                            <div className="text-box">
                                <textarea id="poster" placeholder="Comment..." onChange={e => this.setState({new_post: e.target.value})} value={this.state.new_post} onKeyDown={this.adjustInput}></textarea>
                                <p className="respond" id="comment_button" onClick={this.postComment}>Comment</p>
                            </div>
                        </div>

                        {this.displayPosts()}

                    </div>
                </div>
            </div>
        );
    }
}


ReactDOM.render(
  <Thread />,
  document.getElementById("thread_container")
);