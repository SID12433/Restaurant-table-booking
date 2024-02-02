import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
import { RestaurantlistComponent } from './restaurantlist/restaurantlist.component';
import { RestaurantdetailComponent } from './restaurantdetail/restaurantdetail.component';
import { ReservationComponent } from './reservation/reservation.component';
import { ReservationstatusComponent } from './reservationstatus/reservationstatus.component';

const routes: Routes = [
  {path:"register",component:RegisterComponent},
  {path:"",component:LoginComponent},
  {path:"restaurants",component:RestaurantlistComponent},
  {path:"restaurants/:id",component:RestaurantdetailComponent},
  {path:"restaurants/:id/reservation",component:ReservationComponent},
  {path:"status",component:ReservationstatusComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
