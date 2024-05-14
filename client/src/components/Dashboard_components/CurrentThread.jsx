import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Link } from 'react-router-dom';
import CreatePost from '../post_components/CreatePost';
import { useUser } from '../UserContext';
import Navbar from '../Navbar';

function CurrentThread() {

    const { userName, userAvatar } = useUser();

    const [currentThread, setCurrentThread] = useState({
        thread_title: '',
        thread_content: '',
        posts: [],
        likes: ''
    });

    const [favThread, setFavThread] = useState(false)
    console.log(favThread);
    console.log(currentThread)
    const { id } = useParams();


    function handleNewPost(newPost) {
        console.log(newPost); 
        if (newPost && newPost.id) {
            setCurrentThread(prevThread => ({
                ...prevThread,
                posts: [...prevThread.posts, newPost]
            }));
        } else {
            console.error('Attempted to add an undefined or invalid Post:', newPost);
        }
    };

    function handleFavThread() {
        setFavThread(!favThread)
        console.log(favThread)
        

            fetch(`http://localhost:5555/favorites`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    user_id: 'user.id',
                    thread_id: id
                })
            }).then(res => {
                if (res.status!= 200) {
                    console.log("EROEROEROR");
                    return;
                }
                res.json().then(data => {
                    if (data!= null) {
                        setCurrentThread(data)
                        console.log(data);
                    }
                });
            })
    }

    useEffect(() => {
        fetch(`http://localhost:5555/threads/${id}`)
            .then(response => response.json())
            .then(data => {
                console.log(data.posts)
                console.log(data.posts.user)
                setCurrentThread(prevState => ({
                    ...prevState, 
                    ...data
                }));
            });
    }, [id]);

    return (
    <div>
        <div>
            <Navbar />
        </div>
        <h1>{currentThread.thread_title}</h1>
        <h2>{currentThread.thread_content}</h2>
        <h4>{userName}</h4>
        <img src={userAvatar} alt="Profile"></img>
        <button onClick = {handleFavThread}>❤️</button>
        <div className='CurrentThread'>
          {currentThread.posts && currentThread.posts.map(post => (
              <div className="PostContainer" key={post.id}>
                    <p>{post.user.user_name}</p>
                    <img src={post.user.user_avatar} alt="User Avatar" />
                    <p>Posted by: {post.user.user_name}</p>
                    <p>{post.content}</p>
                    <i>❤️ {post.likes}</i>
              </div>
          ))}
        </div>
        <CreatePost onAddPost={handleNewPost} threadId={id} />
        
    </div>
    )


}

export default CurrentThread;
