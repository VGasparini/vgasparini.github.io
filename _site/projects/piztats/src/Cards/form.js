import React from 'react';

const Form = props =>{
    return(
        <div className="jumbotron bg-light">
          <form>
            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <label class="input-group-text" for="inputName">Name</label>
              </div>
              <input type="text" class="form-control" placeholder="Pizzaria do Gasparini" aria-label="Pizzaria do Gasparini" aria-describedby="basic-addon1"></input>
            </div>

            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <label class="input-group-text" for="inputSize">Size</label>
              </div>
              <select class="custom-select" id="inputSize">
                <option selected>Choose...</option>
                <option value="30">30 cm</option>
                <option value="35">35 cm</option>
                <option value="40">40 cm</option>
                <option value="45">45 cm</option>
                <option value="50">50 cm</option>
              </select>
            </div>

            <div class="input-group mb-3">
              <div class="input-group-prepend">
                <span class="input-group-text">R$</span>
              </div>
              <input type="number" class="form-control" aria-label="Amount" min="0" ></input>
              <div class="input-group-append">
                <span class="input-group-text">.00</span>
              </div>
            </div>

            <div class="input-group mb-3 justify-content-center">
              <div class="input-group-prepend">
                <span class="input-group-text">Drink included?</span>
              </div>
              <div class="input-group-text">
                <input type="checkbox" aria-label="Checkbox and fill if have coke included"></input>
              </div>
            </div>
          </form>

          <div class="input-group mb-2 justify-content-center">
            <button type="button" class="btn btn-success mx-2">Add</button>
            <button type="button" class="btn btn-danger mx-2">Clear</button>
          </div>

        </div>
    );
}

export default Form;