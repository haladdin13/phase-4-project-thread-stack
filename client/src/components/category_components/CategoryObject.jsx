import React, { useState, useEffect } from 'react';

function CategoryObject({
    id,
    category_name,
    description,
    user_id
}){



    return(
        <div>
            <h1>{category_name}</h1>
            <p>ID: {id}</p>
            <p>Description: {description}</p>
            <p>User ID: {user_id}</p>
        </div>
    )
}

export default CategoryObject;