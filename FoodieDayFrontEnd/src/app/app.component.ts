import { Component, OnInit } from '@angular/core';
import { UserService } from './service/user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'FoodieDayFrontEnd';
  islogged:boolean=false

  constructor(private service:UserService){

  }

  ngOnInit(): void {
    this.service.is_authenticated.subscribe(res=>this.islogged=res)
  }
}
