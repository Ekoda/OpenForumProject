class Thread extends React.Component {
    constructor(p) {
        super(p);

        this.state = {
            thread: window.location.pathname.substring(1),
            posts: [],
        }
    }

    componentDidMount() {
        const url = window.location.origin + "/api/posts/" + this.state.thread
        fetch(url)
        .then(response => response.json())
        .then(data => this.setState({posts: data.posts}))
        
    }

    displayPosts = () => {
        const posts = this.state.posts
        return (
            <div>
                {posts.map((post) => 
                    <div className="comment"> 
                        <img className="userpic" src={post.image}/>
                        <div className="text-box">
                            <h4 className="username" style={{color: post.color}}>{post.username}</h4>
                            <p>{post.body}</p>
                            <textarea className="responseinput" type="text" placeholder="Respond..."></textarea>
                            <div className="comment-interact">
                            <p className="numbers">{post.score}</p><i className="fas fa-light fa-chevron-up"></i> <i className="fas fa-light fa-chevron-down"></i><p className="timer">{ moment(post.timestamp).fromNow()}</p> <p id={post.id} className="respond">Respond</p>
                            </div>
                        
                            {post.responses.map((response) =>
                                <div className="response-box">
                                <img className="responsepic" src={response.image}/>
                                <div className="response-text"> 
                                    <h5 className="username" style={{ color: response.color }}>{ response.username }</h5>
                                    <p><span className="at username">{ "#" + response.response_to_username }</span> { response.body }</p>
                                    <textarea className="responseinput" type="text" placeholder="Respond..."></textarea>
                                    <div className="comment-interact">
                                        <p className="numbers">{ response.score }</p>
                                        <i className="fas fa-light fa-chevron-up"></i>
                                        <i className="fas fa-light fa-chevron-down"></i>
                                        <p className="timer">{ moment(response.timestamp).fromNow() }</p>
                                        <p id={response.id} className="respond">Respond</p>
                                    </div>
                                </div>
                            </div>
                            
                            )}

                        </div>
                    </div>
                )}
            </div>)
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
                                <textarea id="poster" placeholder="Comment..."></textarea>
                                <p className="respond" id="comment">Comment</p>
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