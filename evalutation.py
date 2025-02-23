from sklearn.metrics import classification_report, confusion_matrix
import json
import argparse
import os

from utils.data_utils import load_data


def print_evaluation_results(predictions, gt_labels, num_of_classes=3):
    if num_of_classes == 3:
        target_names = ['refutes', 'supports', 'not enough info']
        label_map = {'refutes': 0, 'supports': 1, 'not enough info': 2}
        labels = [label_map[e] for e in gt_labels]
        predictions = [label_map[e] for e in predictions]
        print(classification_report(labels, predictions, target_names=target_names, digits=4))
        print(confusion_matrix(labels, predictions))
        print()
    elif num_of_classes == 2:
        target_names = ['refutes', 'supports']
        label_map = {'refutes': 0, 'supports': 1}
        labels = [label_map[e] for e in gt_labels]
        predictions = [label_map[e] for e in predictions]
        print(classification_report(labels, predictions, target_names=target_names, digits=4))
        print(confusion_matrix(labels, predictions))
        print()


def evaluate_hover_by_hops(result_file):
    results = load_data(result_file)

    predictions = {'2_hop': [], '3_hop': [], '4_hop': []}
    gt_labels = {'2_hop': [], '3_hop': [], '4_hop': []}
    for sample in results:
        key = f"{sample['num_hops']}_hop"
        gt_labels[key].append(sample['label'].strip())
        predictions[key].append(sample['prediction'].strip())

    for key in predictions:
        print(key)
        print_evaluation_results(predictions[key], gt_labels[key], num_of_classes=2)
        print()


def evaluate_feverous(result_file):
    results = load_data(result_file)

    predictions = []
    gt_labels = []
    for sample in results:
        gt_labels.append(sample['label'].strip())
        predictions.append(sample['prediction'].strip())
    
    print_evaluation_results(predictions, gt_labels, num_of_classes=2)


def parse_args():
    parser = argparse.ArgumentParser()
    # dataset args
    parser.add_argument('--dataset_name', type=str, default='HOVER')
    parser.add_argument('--result_file', type=str, default='')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    if args.dataset_name == 'FEVEROUS':
        evaluate_feverous(args.result_file)
    elif args.dataset_name == 'HOVER':
        evaluate_hover_by_hops(args.result_file)
    else:
        raise NotImplementedError
