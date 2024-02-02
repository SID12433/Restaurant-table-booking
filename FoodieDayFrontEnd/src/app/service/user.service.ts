import { Injectable, OnInit } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http"
import { BehaviorSubject, Observable, tap } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService implements OnInit{

  public is_authenticated=new BehaviorSubject<boolean>(false)


  constructor(private http:HttpClient) { 

  }

  ngOnInit(): void {
      
  }
  signUp(data:any){
    return this.http.post("http://127.0.0.1:8000/api/register/",data)
  }
  getToken(data:any){
    return this.http.post("http://127.0.0.1:8000/api/token/",data).pipe(tap(data=>this.is_loggedIn()))
  }

  getRestaurants(){
    if("token" in localStorage){
      let token:any=localStorage.getItem("token")
      let headers=new HttpHeaders({
          "Authorization": token,
          "Content-Type": "application/json"
      })
      return this.http.get("http://127.0.0.1:8000/api/restaurant/",{headers})
    }
    else{
      return new Observable()
    }

  }
  retrieveRestaurant(id:number){
    if("token" in localStorage){
      let token:any=localStorage.getItem("token")
      let headers=new HttpHeaders({
          "Authorization": token,
          "Content-Type": "application/json"
      })
      return this.http.get(`http://127.0.0.1:8000/api/restaurant/${id}/`,{headers})
    }
    else{
      return new Observable()
    }

  }

  reservation(id:number,data:any){
    if("token" in localStorage){
      let token:any=localStorage.getItem("token")
      let headers=new HttpHeaders({
          "Authorization": token,
          "Content-Type": "application/json"
      })
      return this.http.post(`http://127.0.0.1:8000/api/restaurant/${id}/create_reservation/`,data,{headers})
    }
    else{
      return new Observable()
    }

  }

  is_loggedIn(){
    this.is_authenticated.next("token" in localStorage?true:false)
  }


}
