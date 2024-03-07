import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function CurrentCategory({
    category_name,
    description,
    threads,
    user_id
}) {
    const [categoryThread, setCategoryThread] = useState({
        category_name: '',
        description: '',
        threads: [],
        user_id: ''
    });
    console.log(categoryThread)
    const { id } = useParams();

    useEffect(() => {
        fetch(`http://localhost:5555/categories/${id}`)
            .then(response => response.json())
            .then(data => {
                console.log(data.threads)
                setCategoryThread(prevState => ({
                    ...prevState, // Use prevState to ensure you're correctly updating the state based on its previous value
                    ...data // This updates the state with fetched data, assuming data structure matches your state
                }));
            });
    }, [id]);

    return (
        <div>
        <h1>{categoryThread.category_name}</h1>
        <h2>{categoryThread.description}</h2>
        <div>
          {categoryThread.threads && categoryThread.threads.map(thread => (
              <div>
                    <h3 key={thread.id}>{thread.thread_title}</h3>
                    <p>{thread.thread_content}</p>
              </div>
          ))}
        </div>
    </div>
    )


}

export default CurrentCategory;
