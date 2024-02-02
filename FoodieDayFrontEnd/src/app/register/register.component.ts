import { Component } from '@angular/core';
import { UserService } from '../service/user.service';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';



@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  constructor(private service:UserService,private route:Router){
  }

  regForm=new FormGroup({
    username:new FormControl("",Validators.required),
    email:new FormControl("",Validators.required),
    password:new FormControl("",Validators.required),
    phone:new FormControl("",Validators.required),
    address:new FormControl("",Validators.required),
  })

  register(){
    if(this.regForm.valid){
      let data=this.regForm.value
      // console.log(data) 
      this.service.signUp(data).subscribe(data=>{
        this.route.navigateByUrl("login")
      })
      
    }
  }

}
