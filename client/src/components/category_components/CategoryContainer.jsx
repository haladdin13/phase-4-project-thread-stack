import React from 'react';
import CategoryObject from './CategoryObject';

function CategoryContainer({renderCategory}){

    const categoryToRender = renderCategory.map((categoryObj) => {
        return(
            <div key={categoryObj.id}>
                <CategoryObject {...categoryObj} />
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