import React, {useState, useEffect} from 'react';
import ThreadContainer from './Dashboard_components/Thread_Container';
import CreateThread from './Dashboard_components/Create_Thread';
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

    return(
        <div>
            <CreateThread onAddThread={addThread} />
            <ThreadContainer threads={threads}/>
        </div>
    )
}

export default Dashboard;