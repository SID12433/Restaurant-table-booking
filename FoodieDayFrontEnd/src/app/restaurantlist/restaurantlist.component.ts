import { Component, OnInit } from '@angular/core';
import { UserService } from '../service/user.service';

@Component({
  selector: 'app-restaurantlist',
  templateUrl: './restaurantlist.component.html',
  styleUrls: ['./restaurantlist.component.css']
})
export class RestaurantlistComponent implements OnInit {

  restaurants:any
  constructor(private service:UserService){

  }
  ngOnInit(): void {
      this.service.getRestaurants().subscribe(data=>this.restaurants=data)
  }

}
