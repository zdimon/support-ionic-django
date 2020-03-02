import { CommonHttpClient } from './../http.service';
import { Component, OnInit, Output, EventEmitter, Input } from '@angular/core';
import { API_URL } from '../globals';

@Component({
  selector: 'app-form-comment',
  templateUrl: './form.comment.html',
  styleUrls: ['./task.component.scss'],
})
export class FormCommentComponent implements OnInit {
  content: string;
  @Input() taskId: number;
  @Output() commentAdded = new EventEmitter<number>();
  constructor(private http: CommonHttpClient) { }

  ngOnInit() {}

  commentForm = () => {

    var data = {
      task_id: this.taskId,
      content: this.content
    };
    this.http.post(API_URL + '/mobile_api/save_comment', data).subscribe((data: any) => {
       this.content = '';
       this.commentAdded.emit(this.taskId);
    });
  }

}
