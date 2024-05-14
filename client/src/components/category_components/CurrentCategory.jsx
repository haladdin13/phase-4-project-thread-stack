import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { Link } from 'react-router-dom';
import CreateThread from '../Dashboard_components/Create_Thread';
import Navbar from '../Navbar';
function CurrentCategory({
    category_name,
    description,
    user_id
}) {
    const { id } = useParams();
    const [threads, setThreads] = useState({
        thread_title: '',
        thread_content: '',
        category_id: id,
        likes: ''
    })
    
    const [categoryThread, setCategoryThread] = useState({
        category_name: '',
        description: '',
        threads: [],
        user_id: ''
    });
    console.log(categoryThread)

    const addThread = (newThread) => {
        console.log(newThread);
        if (newThread && newThread.id){
            setCategoryThread(prevCategory => ({
                ...prevCategory,
                threads: [...prevCategory.threads, newThread]
        }));
        } 
        else {
            console.error(" Invalid Thread:", newThread);
        }
    };

    useEffect(() => {
        fetch(`http://localhost:5555/categories/${id}`)
            .then(response => response.json())
            .then(data => {
                console.log(data.threads)
                setCategoryThread(prevState => ({
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
        <h1>{categoryThread.category_name}</h1>
        <h2>{categoryThread.description}</h2>
        <CreateThread onAddThread={addThread} categoryID={id}/>
        <div className='CurrentCategory'>
          {categoryThread.threads && categoryThread.threads.map(thread => (
              <div className="ThreadContainer">
                <Link to={`/threads/${thread.id}`}>
                    <h3 key={thread.id}>{thread.thread_title}</h3>
                </Link>
                    <p>{thread.thread_content}</p>
              </div>
          ))}
        </div>
    </div>
    )


}

export default CurrentCategory;
