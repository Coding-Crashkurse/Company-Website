import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';

@Component({
  standalone: true,
  selector: 'app-udemy',
  templateUrl: './udemy.component.html',
  styleUrls: ['./udemy.component.css'],
  imports: [CommonModule, MatCardModule, MatButtonModule],
})
export class UdemyComponent implements OnInit, OnDestroy {
  promoCode = 'PROMO123';
  promoLink =
    'https://www.udemy.com/course/angular-advanced/?couponCode=PROMO123';
  timeLeft = '';
  private timer: any;

  ngOnInit(): void {
    // Example: Expires in 1 hour
    const expiry = Date.now() + 3600_000;
    this.startCountdown(expiry);
  }

  startCountdown(expiryTime: number) {
    this.timer = setInterval(() => {
      const diff = expiryTime - Date.now();
      if (diff <= 0) {
        this.timeLeft = 'Promo expired!';
        clearInterval(this.timer);
        return;
      }
      const minutes = Math.floor((diff / 1000 / 60) % 60);
      const seconds = Math.floor((diff / 1000) % 60);
      this.timeLeft = `Expires in ${minutes}m ${seconds}s`;
    }, 1000);
  }

  ngOnDestroy(): void {
    if (this.timer) {
      clearInterval(this.timer);
    }
  }
}
