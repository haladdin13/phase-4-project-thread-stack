import React, {useState, useEffect} from 'react';
import ThreadContainer from './Dashboard_components/Thread_Container';
import CreateThread from './Dashboard_components/Create_Thread';
import CurrentCategory from './category_components/CurrentCategory';
function Dashboard(){

    const [threads, setThreads] = useState([])
    
    const addThread = (newThread) => {
        console.log(newThread);
        if (newThread && newThread.id){
            setThreads(prevThreads => [...prevThreads, newThread]);
        } 
        else {
            console.error(" Invalid Thread:", newThread);
        }
    };
    

    useEffect(() => {
        fetch("http://127.0.0.1:5555/threads").then(res => {
            if (res.status != 200){
                console.log("EROEROEROR");
                return;
            }
            res.json().then(data => {
                if (data != null){
                    setThreads(data)
                    console.log(data);
                }
            });
        })
    }, [setThreads]);

    function handleSaveThread(id, updatedThread){
        fetch(`http://localhost:5555/threads/${id}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedThread),
        })
     .then(res => res.json())
     .then(data => {

        setThreads(prevThreads => prevThreads.map(thread => 
            thread.id === data.id ? data : thread
        ));
    })
    }

    function handleDeleteThread(id) {
        fetch(`http://localhost:5555/threads/${id}`, {
            method: 'DELETE',
        })
        .then(response => {
                setThreads(prevThreads => 
                    prevThreads.filter(thread => thread.id !== id)
                );
        })
    }


    return(
        <div>
            <CreateThread onAddThread={addThread} />
            <ThreadContainer threads={threads} onSave={handleSaveThread} onDelete={handleDeleteThread}/>

            
        </div>
    )
}

export default Dashboard;