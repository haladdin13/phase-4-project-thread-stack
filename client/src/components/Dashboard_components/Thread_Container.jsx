import React from 'react';
import ThreadObject from './Thread_Object';

function ThreadContainer({threads, onSave}){

    const threadToRender = threads.map((threadObj) => {
        return(
            <div key={threadObj.id}>
                <ThreadObject {...threadObj} onSave={onSave}/>
            </div>
        )
    })
    
    return(
        <div>
            <h1>Threads</h1>
            {threadToRender}
        </div>
    )
}

export default ThreadContainer;