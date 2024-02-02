import { Component, OnInit } from '@angular/core';
import { UserService } from '../service/user.service';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private service:UserService,private route:Router){

  }
  ngOnInit(): void {
      
  }

  loginForm=new FormGroup({
    username:new FormControl("",Validators.required),
    password:new FormControl("",Validators.required),
  })

  
  login(){
    if(this.loginForm.valid){
      let data=this.loginForm.value
      this.service.getToken(data).subscribe(data=>{
        if("token" in data){
          localStorage.setItem("token",`Token ${data.token}`)
          this.route.navigateByUrl("restaurants")  
        }
      })    
    }
  }

}
