import React, {useState, useEffect} from 'react';
import ThreadContainer from './Dashboard_components/Thread_Container';
import CategoryContainer from './category_components/CategoryContainer';

function Dashboard(){
    const [threads, setThreads] = useState([])
    
    

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
            <ThreadContainer threads={threads}/>
        </div>
    )
}

export default Dashboard;