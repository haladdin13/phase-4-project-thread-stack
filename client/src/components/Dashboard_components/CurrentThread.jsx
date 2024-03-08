import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Link } from 'react-router-dom';
import CreatePost from '../post_components/CreatePost';

function CurrentThread({
    thread_title,
    thread_content,
    category_id,
    posts,
    likes
}) {
    const [addPost, setAddPost] = useState([]);
    const [currentThread, setCurrentThread] = useState({
        thread_title: '',
        thread_content: '',
        posts: [],
        likes: ''
    });
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

    useEffect(() => {
        fetch(`http://localhost:5555/threads/${id}`)
            .then(response => response.json())
            .then(data => {
                console.log(data.posts)
                setCurrentThread(prevState => ({
                    ...prevState, // Use prevState to ensure you're correctly updating the state based on its previous value
                    ...data // This updates the state with fetched data, assuming data structure matches your state
                }));
            });
    }, [id]);

    return (
        <div>
        <h1>{currentThread.thread_title}</h1>
        <h2>{currentThread.thread_content}</h2>
        <div className='CurrentThread'>
          {currentThread.posts && currentThread.posts.map(post => (
              <div className="PostContainer" key={post.id}>
                    <p>{post.content}</p>
                    <i>❤️ {currentThread.likes}</i>
              </div>
          ))}
        </div>
        <CreatePost onAddPost={handleNewPost} threadId={id} />
        
    </div>
    )


}

export default CurrentThread;
