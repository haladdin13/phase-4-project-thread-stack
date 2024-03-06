import React, {useState, useEffect} from "react";
import CategoryContainer from "./category_components/CategoryContainer";
import CreateCategory from "./category_components/CreateCategory";
import CategoryObject from "./category_components/CategoryObject";


function Category(){

    return(
        <div>
            <CreateCategory />
            <CategoryContainer />
            <CategoryObject />
        </div>
    )
}

export default Category;