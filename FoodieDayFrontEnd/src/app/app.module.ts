import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {HttpClientModule} from "@angular/common/http";
import { RegisterComponent } from './register/register.component'
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { LoginComponent } from './login/login.component';
import { RestaurantlistComponent } from './restaurantlist/restaurantlist.component';
import { RestaurantdetailComponent } from './restaurantdetail/restaurantdetail.component';
import { FooterComponent } from './footer/footer.component';
import { NavComponent } from './nav/nav.component';
import { ReservationComponent } from './reservation/reservation.component';
import { ReservationstatusComponent } from './reservationstatus/reservationstatus.component';

@NgModule({
  declarations: [
    AppComponent,
    RegisterComponent,
    LoginComponent,
    RestaurantlistComponent,
    RestaurantdetailComponent,
    FooterComponent,
    NavComponent,
    ReservationComponent,
    ReservationstatusComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
