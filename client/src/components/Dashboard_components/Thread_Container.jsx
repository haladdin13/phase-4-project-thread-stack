import React from 'react';
import ThreadObject from './Thread_Object';

function ThreadContainer({threads}){

    const threadToRender = threads.map((threadObj) => {
        return(
            <div key={threadObj.id}>
                <ThreadObject{...threadObj}/>
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