import { NgClass } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { UserService } from '../service/user.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-reservation',
  templateUrl: './reservation.component.html',
  styleUrls: ['./reservation.component.css']
})
export class ReservationComponent implements OnInit{

  id:any
  time:any
  people_count:number=1
  date:any

  constructor(private service:UserService,private router:Router,private route:ActivatedRoute){

      this.id=this.route.snapshot.params["id"]
  }

  ngOnInit(): void {
    
    
  }

  makereservation(){
    let data={"time":this.time,"date":this.date,"people_count":this.people_count}
    this.service.reservation(this.id,data).subscribe(data=>console.log(data))
    this.router.navigateByUrl("status")
  }

}
