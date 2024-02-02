import { Component, OnInit } from '@angular/core';
import { UserService } from '../service/user.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-restaurantdetail',
  templateUrl: './restaurantdetail.component.html',
  styleUrls: ['./restaurantdetail.component.css']
})
export class RestaurantdetailComponent implements OnInit {

  restaurant:any
  id:any
  constructor(private route:ActivatedRoute,private service:UserService,private router:Router){
    this.id=this.route.snapshot.params["id"]    
  }

  ngOnInit(): void {
    this.service.retrieveRestaurant(this.id).subscribe(data=>this.restaurant=data)
    console.log(this.restaurant);
    
  }

}
