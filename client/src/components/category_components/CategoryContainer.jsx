import React from 'react';
import CategoryObject from './CategoryObject';

function CategoryContainer({renderCategory, onSave, onDelete}){

    const categoryToRender = renderCategory.map((categoryObj) => {
        return(
            <div key={categoryObj.id}>
                <CategoryObject {...categoryObj} onSave={onSave} onDelete={onDelete}/>
            </div>
        )
    })

    return(
        <div>
            <h1>Categories</h1>
            {categoryToRender}
        </div>
    )
}

export default CategoryContainer;